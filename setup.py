import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
          name="streamer",
	  version="1.0",
          author="Udit Namdev",
	  author_email="unamdev0@gmail.com",
	  description="Stream movies directly from torrent without downloading",
          long_description = long_description,
          long_description_content_type="text/markdown",
	  url="https://github.com/unamdev0/streamer",
	  license='MIT',
	  packages=["streamer"],
	  scripts=["streamer"],
        keywords = ['Torrent', 'Stream', 'Movies','Series','Streamer','Magnet link','utorrent','piratebay','yify'], 
          classifiers=[
                "Programming Language :: Python :: 3",
                "License :: OSI Approved :: MIT License",
                "Operating System :: OS Independent",
          ],
	  install_requires=[
		  'BeautifulSoup4',
		  'requests'],
	  zip_safe=False)
