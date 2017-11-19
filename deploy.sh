#!/bin/bash
tar cvf secrets.tar .config_secret
travis encrypt-file secrets.tar -a -f
