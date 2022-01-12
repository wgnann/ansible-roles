# ansible-roles
Repositórios de roles que usamos em nossos playbooks. Os roles de Windows possuem prefixo `win_`.

## autofs
Configura autofs com um mount point por grupo. Não usa, ainda, o unburden para os mounts de NFS.

## base
Repositórios, pacotes e chaves de SSH.

## classroom
Depende do role `ui`. Lida com pacotes, autologin e screensaver. Usa a variável `classroom_user_password` para definir a senha do usuário de autologin.

## lab
Também depende do role `ui`. Pacotes.

## pam_mount
Cuida da montagem das homes usando o pam_mount. Existem dois tipos cuja configuração depende de o usuário residir no grupo `nfshome`:
  - monta num diretório na área de trabalho;
  - monta a home inteira.

## ssh
Grupos autorizados e portas para SSH.

## sssd
Configuração de autenticação usando SSSD como meio para LDAP+Kerberos. Precisa que a keytab da máquina seja criada e esteja disponível no diretório `files/keytabs`. Usa o fact `ansible_hostname` para referenciar a keytab.

## ui
Pacotes e arcabouço de customização do dconf.
