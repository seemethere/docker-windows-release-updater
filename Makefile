ifndef BASE_URL
$(error BASE_URL is not set)
endif

ifndef RELEASE_NAME
$(error RELEASE_NAME is not set)
endif

ifndef RELEASE_CHANNEL
$(error RELEASE_CHANNEL is not set)
endif

ifndef RELEASE_URL
$(error RELEASE_URL is not set)
endif

all: clean update

clean:
	rm -rf build

.PHONY: update
update:
	mkdir -p build
	docker build -t docker-windows-release-updater .
	docker run \
		-e BUCKET_NAME \
		--rm docker-windows-release-updater $(BASE_URL) $(RELEASE_NAME) $(RELEASE_CHANNEL) $(RELEASE_URL) | tee build/index.json
