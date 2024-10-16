#利用するUbuntuのイメージ
FROM ubuntu:20.04

# 使うコマンドをインストール
RUN \
    apt update && \
    apt -y upgrade && \
    apt install -y tzdata && \
    apt install -y build-essential && \
    apt install -y software-properties-common && \
    apt install -y curl git man unzip vim wget sudo && \
    apt install -y iputils-ping net-tools && \
    apt install -y gcc g++ make cmake 

# rootだと色々と不便なので，ユーザーを作成
RUN useradd -m user
# ルート権限を付与
RUN gpasswd -a user sudo
# パスワードはuserに設定
RUN echo 'user:user' | chpasswd
# sshログイン時のシェルをbashに設定
RUN sudo sed -i 's/user:x:1000:1000::\/home\/user:\/bin\/sh/user:x:1000:1000::\/home\/user:\/bin\/bash/g' /etc/passwd

# sshするための設定（公式サイト参考）
RUN apt install -y openssh-server
RUN mkdir /var/run/sshd
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd
ENV NOTVISIBLE="in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile
EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]