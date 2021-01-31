# App #

## Requirements for running the app
---
* docker
* docker-compose
That's it!

## How do I get set up? ##
---
* Copy `doc/sample_files/example.env` to the root of the repository and edit it to set the configurations for this specific install and rename to `.env`.
* (optional) Edit the docker-compose file to fit your needs (such as which folders are linked to the local filesystem and where the docker containers are stored)
* Run this in the main folder:
```
docker-compose up -d
```
All done! This will build the app and start all the necessary services. Check out `localhost:80`!


## Additional documentation is found at:
---
See `docs/`.


## Who do I talk to in case of problems? ##

* Santiago Espinosa Mooser
  * [keybase](https://keybase.io/santiagoespinosa)
  * [email](santiago.mooser@pm.me)