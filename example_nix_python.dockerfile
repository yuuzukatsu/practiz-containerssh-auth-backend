FROM containerssh/agent AS agent

FROM nixos/nix:latest
COPY --from=agent /usr/bin/containerssh-agent /usr/bin/containerssh-agent
#CMD ["sleep", "infinity"]
RUN nix-shell -p python3
