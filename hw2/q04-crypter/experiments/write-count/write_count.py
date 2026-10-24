import pyinotify
import sys

class EventHandler(pyinotify.ProcessEvent):
    def __init__(self, filename):
        super().__init__()
        self.filename = filename
        self.write_count = 0

    def process_IN_MODIFY(self, event):
        if event.pathname == self.filename:
            self.write_count += 1
            print(f"File '{self.filename}' written to. Total writes: {self.write_count}")

def count_file_writes(filepath):
    wm = pyinotify.WatchManager()
    notifier = pyinotify.Notifier(wm, EventHandler(filepath))
    wdd = wm.add_watch(filepath, pyinotify.IN_MODIFY)

    try:
        print(f"Monitoring '{filepath}' for write events...")
        notifier.loop()
    except KeyboardInterrupt:
        print("\nMonitoring stopped.")
    finally:
        notifier.stop()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python count_writes.py <filepath>")
        sys.exit(1)

    file_to_monitor = sys.argv[1]
    count_file_writes(file_to_monitor)
