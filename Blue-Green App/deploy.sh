#!/bin/bash
echo "Starting Blue-Green Deployment..."

# Stop old system
docker compose down

# Run new system  
docker compose up -d

echo "Deployment Completed!"