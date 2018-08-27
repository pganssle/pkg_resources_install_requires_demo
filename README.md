# pkg_resources demo script
This is a script to demonstrate the somewhat aggressive dependency-checking behavior of `pkg_resources`.

Start by installing `pkg2`, then `pkg1` and `pkg3` in a virtualenv. For convenience, you can use `source initial_install.sh` to do this part for you.

Demonstrate the normal behavior:

```bash
$ pkg1script
Used from pkg2
$ pkg3script
Used from pkg2
```

Now uninstall `pkg2` - `pkg1` declares this as an `install_requires` dependency but `pkg3` does not. Other than that `pkg1` and `pkg3` are identical:

```bash
pip uninstall pkg2
```

Now if you try to run `pkg3script` it still works just fine:

```bash
$ pkg3script
Fell back to pkg1
```

But if you try to run `pkg1script` it will fail:

```bash
$ pkg1script
Traceback (most recent call last):
...
pkg_resources.DistributionNotFound: The 'pkg2' distribution was not found and is required by pkg1
```
