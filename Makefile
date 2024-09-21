# Filename: Makefile

RUNTIME=docker
IMAGE=little-lemon-restaurant
IMAGE_TAG=latest
IMAGE_NAME=$(IMAGE):$(IMAGE_TAG)

.PHONY: image-run
image-run: image-build
	$(RUNTIME) run -it --rm -p 8000:8000 $(IMAGE_NAME)

.PHONY: image-build
image-build:
	$(RUNTIME) build -t $(IMAGE_NAME) .

.PHONY: clean
clean:
	$(RUNTIME) rmi $(IMAGE_NAME)
