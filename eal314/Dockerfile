FROM python:3.12-slim
COPY turnier_action.py /turnier_action.py
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
