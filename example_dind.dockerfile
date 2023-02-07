FROM containerssh/agent AS agent

FROM docker:dind
COPY --from=agent /usr/bin/containerssh-agent /usr/bin/containerssh-agent
# CMD ["sleep", "infinity"]