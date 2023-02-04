FROM containerssh/agent AS agent

FROM nixos/nix:latest
COPY --from=agent /usr/bin/containerssh-agent /usr/bin/containerssh-agent
#CMD ["sleep", "infinity"]
CMD ["/usr/bin/containerssh-agent", "wait-signal", "--signal", "INT", "--signal", "TERM"]
