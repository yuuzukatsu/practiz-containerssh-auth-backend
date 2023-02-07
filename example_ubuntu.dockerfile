FROM containerssh/agent AS agent

FROM ubuntu:latest
COPY --from=agent /usr/bin/containerssh-agent /usr/bin/containerssh-agent
# CMD ["sleep", "infinity"]