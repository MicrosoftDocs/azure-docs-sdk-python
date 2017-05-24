Installation
============

Installation with pip
---------------------

You can install each Azure service's library individually:

```console
$ pip install azure-batch          # Install the latest Batch runtime library
$ pip install azure-mgmt-scheduler # Install the latest Storage management library
```

Preview packages can be installed using the `--pre` flag:

```console
$ pip install --pre azure-mgmt-compute # will install only the latest Compute Management library
```

You can also install a set of Azure libraries in a single line using the
`azure` meta-package.

```console
$ pip install azure
```

We publish a preview version of this package, which you can access using
the --pre flag:

```console
$ pip install --pre azure
```

Install from Github
-------------------

If you want to install `azure` from source:

    git clone git://github.com/Azure/azure-sdk-for-python.git
    cd azure-sdk-for-python
    python setup.py install

The `dev` branch contains the work in progress.
