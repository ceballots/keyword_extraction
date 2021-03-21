docker-start-jupyter-notebook: docker-build-jupyter
	bash scripts/start_jupyter.sh


docker-build-jupyter:
	docker build --rm -t "jupyter" -f "docker/jupyter_notebook.dockerfile" .

docker-run-baseline: docker-build-baseline
	bash scripts/run_baseline.sh

docker-build-baseline:
	docker build --rm -t "baseline" -f "docker/baseline.dockerfile" .