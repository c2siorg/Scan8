#!/bin/bash
cd Worker
nohup clamd &
sleep 3
nohup python3 app.py &
/bin/bash