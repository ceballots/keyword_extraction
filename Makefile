docker-start-jupyter-notebook: docker-build-jupyter
	bash scripts/start_jupyter.sh


docker-build-jupyter:
	docker build --rm -t "jupyter" -f "docker/Dockerfile" .