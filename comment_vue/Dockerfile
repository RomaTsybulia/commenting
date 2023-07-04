# Frontend Dockerfile

# Base image
FROM node:14-alpine

# Set the working directory inside the container
WORKDIR /app

# Copy the package.json and package-lock.json files to the container
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the frontend source code to the container
COPY . .

# Build the frontend project
RUN npm run build

# Expose the port on which the frontend will run (if applicable)
EXPOSE 8080

# Set the command to run the frontend server (if applicable)
CMD ["npm", "run", "serve"]