.. _hasura_platform:cluster_get-credentials:

Hasura CLI: hasura platform:cluster get-credentials
---------------------------------------------------

Get access credentials for a cluster

Synopsis
~~~~~~~~


Get Kubernetes credentials from hasura.io to access a cluster

::

  hasura platform:cluster get-credentials [flags]

Examples
~~~~~~~~

::

    # Get credentials for a cluster called 'production' in 'hasura/clusters':
    $ hasura cluster get-credentials -c production


Options
~~~~~~~

::

  -c, --cluster string   alias of the cluster to be contacted
  -h, --help             help for get-credentials

Options inherited from parent commands
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

      --project string   hasura project directory where the commands should be executed. (default: current directory)

SEE ALSO
~~~~~~~~

* :ref:`hasura platform:cluster <hasura_platform:cluster>` 	 - Manage hasura clusters

*Auto generated by spf13/cobra*
