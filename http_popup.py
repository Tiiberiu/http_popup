#!/usr/bin/python3 
import json
import time
import http.server
import socketserver
import _thread as thread
from tkinter import Tk, BOTH, X, LEFT
from tkinter.ttk import Frame, Label, Entry, Button


class SimpleDialog(Frame):
    def __init__(self, query_params):
        super().__init__()

        self.outputs = []
        self.entries = []
        self.initUI(query_params)

    def initUI(self, query_params):
        self.master.title("Postman inputs")
        self.pack(fill=BOTH, expand=True)
        frames = []
        lbls = []
        cnt = 0
        for key, value in query_params.items():
            frames.append(Frame(self))
            frames[cnt].pack(fill=X)

            lbls.append(Label(frames[cnt], text=str(key), width=20))
            lbls[cnt].pack(side=LEFT, padx=5, pady=10)

            self.entries.append(Entry(frames[cnt]))
            self.entries[cnt].pack(fill=X, padx=5, expand=True)
            cnt += 1

        frame3 = Frame(self)
        frame3.pack(fill=X)

        # Command tells the form what to do when the button is clicked
        btn = Button(frame3, text="Submit", command=self.onSubmit)
        btn.pack(padx=5, pady=10)
        # print(query_params)

    def onSubmit(self):
        for entry in self.entries:
            self.outputs.append(entry.get())
        self.quit()


class PopupHandler(http.server.BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        return
    def do_GET(self):
        if self.path.startswith("/inputs"):
            # Extract query parameters from the URL
            query_params = self.get_query_params()

            try:
                # Trigger the creation of the popup with query parameters
                popup_outputs = self.create_popup(query_params)
            except Exception as e:
                print(str(e))
                popup_outputs = []
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            key_cnt = 0
            result_dict = {}
            try:
                for key, value in query_params.items():
                    result_dict[key] = popup_outputs[key_cnt]
                    key_cnt += 1
            except Exception as e:
                print(str(e))
                result_dict = {}
            response = json.dumps(result_dict)

            self.wfile.write((response).encode("utf-8"))

    def get_query_params(self):
        # Parse query parameters from the URL
        from urllib.parse import urlparse, parse_qs

        url_parts = urlparse(self.path)
        query_params = parse_qs(url_parts.query)
        return query_params

    def create_popup(self, query_params):
        root = Tk()
        root.geometry("400x450+400+100")
        root.deiconify()
        root.lift()
        root.focus_force()
        root.attributes("-topmost", True)
        root.after_idle(root.attributes, "-topmost", False)
        app = SimpleDialog(query_params)
        root.mainloop()
        try:
            root.destroy()
        except Exception:
            pass
        return app.outputs


def start_server():
    port = 5722
    handler = PopupHandler
    httpd = socketserver.TCPServer(("", port), handler)
    httpd.timeout = 900
    print(f"Server started on port {port}")

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.shutdown()
        print("Server stopped.")


if __name__ == "__main__":
    thread.start_new_thread(start_server, ())
    time.sleep(9999999)
