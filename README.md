```text
# GOATcomms

A lightweight, multi-threaded TCP chat application built in Python. Designed for clean local network communication with automatic peer discovery and dynamic user aliasing.

## Architecture

GOATcomms utilizes a centralized hub-and-spoke TCP socket architecture. The server manages incoming connections, dynamically tracks active user rosters, and broadcasts payloads across connected client threads, while clients maintain asynchronous send-and-receive loops for real-time messaging.


```

+-------------------------------------------------+
|                  GOATcomms Hub                  |
|               (Server / TCP 9999)               |
+-------------------------------------------------+
^                       ^
| (Socket Streams)      | (Socket Streams)
v                       v
+-----------------+     +-----------------+
|   Client Node   |     |   Client Node   |
|   (User: Alice) |     |    (User: Bob)  |
+-----------------+     +-----------------+

```

## Project Structure

* **`server.py`**: Handles incoming TCP socket bindings, manages active client states, tracks unique user handles, and handles real-time message broadcasting and automated user-list synchronization.
* **`client.py`**: Establishes outbound connections, manages local user alias entry, and implements multithreaded stream parsing to keep input prompts clean while receiving inbound broadcasts.

## Getting Started

### Prerequisites

Ensure you have Python 3 installed on your system. No external cryptographic or network libraries are required for the core socket framework.

### Installation & Execution

Clone the repository and spin up the server, then connect one or more clients.

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/mattjslaunwhite/GOATcomms.git](https://github.com/mattjslaunwhite/GOATcomms.git)
   cd GOATcomms

```

2. **Start the server:**
```bash
python server.py

```


3. **Launch a client instance:**
```bash
python client.py

```


*Enter your desired chat alias when prompted, then begin typing messages or type `quit` to exit.*

```

```
