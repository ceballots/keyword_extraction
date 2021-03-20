docker run -ti --rm \
  -p 8888:8888 \
  -v $(pwd)/app \
  jupyter jupyter notebook --no-browser --allow-root --port=8888 --ip=0.0.0.0