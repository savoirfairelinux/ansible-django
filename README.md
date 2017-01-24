# ansible-django

*Provisions a Django project behind nginx/uwsgi, SFL style.*

Running this role results in a fully functional system that can run a Django instance behind [nginx][nginx] and
[uwsgi][uwsgi]. This is used in SFL's project to provision local, staging and production Django instances.
This role doesn't deploy the considered Django project (requirements installation, migrations, ...).
To do so you should use the [ansible-django-deploy][ansible-django-deploy] role and insert it after this `django` role in your playbook.

## Requirements

* Ansible 2.2+
* One of the supported target systems:
  * Ubuntu Xenial
  * Debian Jessie
* For git deployment, you need git
* For SSL with Let's Encrypt, you need [ansible-acme-nginx][ansible-acme-nginx]
* Nginx installed. Recommended role: [ansible-nginx][ansible-nginx]
* MariaDB or PostgreSQL installed and running. Recommended roles:
    * [ansible-mariadb-install][ansible-mariadb-install]
    * [ansible-postgres-install][ansible-postgres-install]
* For MariaDB, we expect passwordless login when `root`. It implies having a `/root/.my.cnf`.

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

### uwsgi touch reload

By default, uwsgi is set up with `touch-reload` set to the root directory of the project (the git
checkout directory). This directory's mtime is generally changed whenever we make a git checkout.
Therefore, with this setting, you shouldn't have to worry about reloading uwsgi after a deploy,
it's done automatically.

[nginx]: https://www.nginx.com/
[uwsgi]: https://github.com/unbit/uwsgi-docs
[ansible-zbackup]: https://github.com/savoirfairelinux/ansible-zbackup
[ansible-backup-cron]: https://github.com/savoirfairelinux/ansible-backup-cron
[ansible-acme-nginx]: https://github.com/hsoft/ansible-acme-nginx
[ansible-nginx]: https://github.com/savoirfairelinux/ansible-nginx
[ansible-mariadb-install]: https://github.com/hsoft/ansible-mariadb-install
[ansible-postgres-install]: https://github.com/savoirfairelinux/ansible-postgres-install
[ansible-django-deploy]: https://github.com/savoirfairelinux/ansible-django-deploy
