FROM containerssh/agent AS agent

FROM httpd:latest
COPY --from=agent /usr/bin/containerssh-agent /usr/bin/containerssh-agent