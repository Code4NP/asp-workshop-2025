# Build Docker (Particpants- Do not run this!)

```sh
docker build -t chasemc2/asp-workshop-2025:latest .

docker push chasemc2/asp-workshop-2025:latest
```

# Run docker command

```sh

docker run -it \
  -p 8080:8080 \
  -e PASSWORD="pass" \
  -e NCBI_KEY=$NCBI_KEY \
  chasemc2/asp-workshop-2025:latest \
    code-server --bind-addr 0.0.0.0:8080 /home/workshop

```

