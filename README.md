# ansible-roles
Repositórios de roles que usamos em nossos playbooks. Os roles de Windows possuem prefixo `win_`.

## base
Repositórios, pacotes e chaves de SSH.

## classroom
Depende do role `ui`. Lida com pacotes, autologin e screensaver. Usa a variável `classroom_user_password` para definir a senha do usuário de autologin.

## lab
Também depende do role `ui`. Pacotes.

## pam_mount
Cuida da montagem das homes usando o pam_mount.

## sssd-ad
Autenticação.

## ssh
Grupos autorizados e portas para SSH.

## ui
Pacotes e arcabouço de customização do dconf.
