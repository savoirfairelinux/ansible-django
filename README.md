# ansible-django

*Provisions a Django project behind nginx/uwsgi, SFL style.*

Running this roles results in a fully functional Django instance running behind [nginx][nginx] and
[uwsgi][uwsgi]. This is used in SFL's project to provision local, staging and production Django
instances.

## Requirements

* Ansible 2.0+
* Debian Jessie on the target system
* A provisioning that runs [ansible-common][ansible-common] before this.

## Conventions

If `django_provide_initial_data` is set, we're expected to have a
`django_initial_data_restore_script` that takes care of importing an initial DB dump and initial
media files into our project. [ansible-zbackup][ansible-zbackup] and
[ansible-backup-cron][ansible-backup-cron] are well suited for this.

## Usage

You call this role as with any other roles. See [vars file](defaults/main.yml) for customisation
options.

Here's an example usage for a local development environment:

```yaml
---
- name: Install a fully functional Django/uwsgi/nginx
  hosts: django-dev

  roles:
    - role: django
      django_debug: yes
      django_user: vagrant
      django_project_symlink_dest: "/vagrant"
```

As you can see, we override `django_debug` because we're in development mode, and we use
`django_project_symlink_dest` to set the project in "symlink mode", which allows us to trigger
live reloads when we edit files on the host.

## Features higlight

All details about the features below are accessibles in the variable files, but here's a highlight.

### Postgres SQL or MariaDB

Your backend can be either Postgres SQL (default) or MariaDB. You can choose your DB with
`django_dbtype`.

### Git clone or symlink

The project's source that lives at `django_project_path` can be either from a git clone or a
symlink. In a "real" environment, you'll want to clone from a git repo, but on a local environment,
you'll want to symlink to your Vagrant share so that your changes to the code are taken into
account immediately. See `django_project_symlink_dest`.

[nginx]: https://www.nginx.com/
[uwsgi]: https://github.com/unbit/uwsgi-docs
[ansible-common]: https://gitlab.savoirfairelinux.com/devops/ansible-common
[ansible-zbackup]: https://github.com/savoirfairelinux/ansible-zbackup
[ansible-backup-cron]: https://github.com/savoirfairelinux/ansible-backup-cron

