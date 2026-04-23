#!/usr/bin/env bash
PORT=${1:-8080}
LOG=/tmp/dashboard_run.log

# If a server is already running on the port, try to detect and fail gracefully
if lsof -iTCP:$PORT -sTCP:LISTEN -P >/dev/null 2>&1; then
  echo "Dashboard already running on port $PORT" | tee -a "$LOG"
  exit 1
fi

echo "Starting OpenClaw Dashboard on port $PORT..." | tee -a "$LOG"
python3 /Users/zcaeth/.openclaw/workspace/openclaw-dashboard-UI/server.py --bind 0.0.0.0 --port "$PORT" >> "$LOG" 2>&1 &
PID=$!
echo $PID > /tmp/openclaw_dashboard_pid.txt
sleep 2
echo "PID=$PID" | tee -a "$LOG"
if ps -p $PID > /dev/null; then
  echo "Server started on port $PORT" | tee -a "$LOG"
else
  echo "Failed to start server" | tee -a "$LOG"
fi
