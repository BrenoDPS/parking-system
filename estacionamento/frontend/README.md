# uiAutopricer

- A template to help you start and manage the uiAutopricer project.

## Project Setup

### Install dependencies

- Run the following command to install all necessary dependencies:

```sh
npm install
```

### Start the Docker Environment

- Navigate to the root directory and run the Docker environment:

```sh
cd ../../
make brsolution
```

### Start the Vue Application

- Serve the Vue application locally:

```sh
npm run serve
```

## Translating with Replexica

### One-Time Setup

- This step needs to be performed only once. Build and run the Replexica environment:

```sh
make replexica_buildrun
```

### Translate

- After setting up, use the following command to start the translation process:

```sh
make replexica_translate
```