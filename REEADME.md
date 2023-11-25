
Monitor Servers
1. **Server Class:**
   - The `Server` class is designed to represent a server with attributes such as `name`, `port`, `connection` type, and `priority`.
   - It has methods:
     - `check_connection()`: Checks the server's connection status using various methods based on the connection type (`plain`, `ssl`, or `ping`).
     - `create_history()`: Records the connection status, success, and timestamp in a history list, keeping a maximum of 100 entries.
     - `ping()`: Sends a ping to the server to check its responsiveness.

2. **Main Script:**
   - The script loads a list of servers from a file named "servers.pickle" using the `pickle` module. If the file doesn't exist or there's an issue loading it, it creates a default list of servers.
   - It then iterates through the list of servers, checks their connection status using the `check_connection()` method, prints the length and last entry of the server's history, and updates the history.
   - Finally, it saves the updated list of servers back to the "servers.pickle" file using `pickle.dump`.

3. **Alert Mechanism (commented out):**
   - There's an alert mechanism using the `email_alert` function, but it's currently commented out. The intention is to send an email alert when a server's connection status changes and the server goes down.

4. **Default Servers:**
   - If the "servers.pickle" file doesn't exist or there's an issue loading it, a default list of servers is created. These servers include Reddit, MSN, Gmail SMTP, a local server (IP: 192.168.1.164), and Yahoo.

Overall, the code provides a basic server monitoring functionality, recording the connection status history and allowing for potential alerting mechanisms when a server goes down.
