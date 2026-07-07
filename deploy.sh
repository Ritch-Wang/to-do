#!/bin/bash
set -e

echo "🚀 Building Lambda container..."
docker build -f docker/Dockerfile.lambda -t todo-lambda .

echo "📦 Tagging image..."
docker tag todo-lambda:latest \
495671352507.dkr.ecr.ap-southeast-2.amazonaws.com/todo-lambda:latest

echo "⬆️ Pushing image..."
docker push 495671352507.dkr.ecr.ap-southeast-2.amazonaws.com/todo-lambda:latest

echo "☁️ Deploying CloudFormation..."
aws cloudformation deploy \
  --template-file infra/sth.yaml \
  --stack-name IAC \
  --capabilities CAPABILITY_NAMED_IAM \
  --parameter-overrides DBPassword=YourPassword

echo "✅ DONE"