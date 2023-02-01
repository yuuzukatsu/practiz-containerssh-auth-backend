FROM containerssh/agent AS agent

FROM node:alpine
COPY --from=agent /usr/bin/containerssh-agent /usr/bin/containerssh-agent
CMD ["sleep", "infinity"]