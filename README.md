# openrave\_models

A repository of humanoid robot models for OpenRAVE.

Currently includes, in alphabetic order:

- [JAXON](/JAXON)
- [JVRC-1](/JVRC-1)
- [Romeo](/Romeo)

## Example

You can run the script ``load_model.py`` to show a given model, for instance:

```bash
$ ipython -i load_model.py JVRC-1/JVRC-1.dae
```

If you prefer to have your OpenRAVE environment in a separate XML file, you can
complete ``environment.xml`` to load a model with the six unactuated degrees of
freedom.
