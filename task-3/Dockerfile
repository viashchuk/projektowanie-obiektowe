FROM ubuntu:24.04

RUN apt-get update && apt-get install -y \
    wget \
    curl \
    software-properties-common \
    unzip \
    zip \
    sqlite3

RUN apt-get install -y openjdk-21-jdk

RUN curl -s "https://get.sdkman.io" | bash
RUN bash -c "source $HOME/.sdkman/bin/sdkman-init.sh \
            && sdk install kotlin \
            && sdk install gradle"

ENV PATH=/root/.sdkman/candidates/kotlin/current/bin:$PATH
ENV PATH=/root/.sdkman/candidates/gradle/current/bin:$PATH

WORKDIR /task-3
COPY . .

CMD ["gradle", "run"]