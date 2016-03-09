# ansible-django

*Provisions a Django project behind nginx/uwsgi, SFL style.*

Running this roles results in a fully functional Django instance running behind [nginx][nginx] and
[uwsgi][uwsgi]. This is used in SFL's project to provision local, staging and production Django
instances.

## Requirements

* Ansible 2.0+
* Debian Jessie on the target system
* A provisioning that runs [ansible-common][ansible-common] before this.

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

[nginx]: https://www.nginx.com/
[uwsgi]: https://github.com/unbit/uwsgi-docs
[ansible-common]: https://gitlab.savoirfairelinux.com/devops/ansible-common

