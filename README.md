# code-analyzer-2


### create credentials

```bash
kubectl create secret generic aws-credentials \
  --from-literal=aws-access-key=YOUR_AWS_ACCESS_KEY_ID \
  --from-literal=aws-secret-key=YOUR_AWS_SECRET_ACCESS_KEY \
  -n code-analyzer
```


```bash
kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml
```