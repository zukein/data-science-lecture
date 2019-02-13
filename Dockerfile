# UPDATE OS
FROM ubuntu:16.04
USER root
ENV HOME /root
ARG VERSION=0.1
ARG MAINTAINER="ScenesK<scenesk.ngt@gmail.com>"

RUN apt update && apt upgrade -y
RUN apt install -y \
    language-pack-ja \
    fonts-takao
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8
ENV TZ Asia/Tokyo

# INSTALL PYTHON
ARG PYTHON_VERSION=3.6.8
ARG PYTHON_ROOT=$HOME/local/python-$PYTHON_VERSION
ENV PATH=$PYTHON_ROOT/bin:$PATH
ARG PYENV_ROOT=$HOME/.pyenv
RUN apt-get install -y \
    git \
    make \
    build-essential \
    libssl-dev \
    zlib1g-dev \
    libbz2-dev \
    libreadline-dev \
    libsqlite3-dev \
    wget \
    curl \
    llvm \
    libncurses5-dev \
    libncursesw5-dev \
    xz-utils \
    tk-dev \
    libffi-dev \
    liblzma-dev && \
    git clone https://github.com/pyenv/pyenv.git $PYENV_ROOT && \
    $PYENV_ROOT/plugins/python-build/install.sh && \
    /usr/local/bin/python-build -v $PYTHON_VERSION $PYTHON_ROOT && \
    rm -rf $PYENV_ROOT

# INSTALL LIBRARY
RUN pip install --upgrade pip && \
    pip install \
    numpy==1.16.0 \
    scipy==1.2.0 \
    statsmodels==0.9.0 \
    scikit-learn==0.20.2 \
    opencv-python==4.0.0.21 \
    lightgbm==2.2.2 \
    tensorflow==1.12.0 \
    pandas==0.23.4 \
    pandas-datareader==0.7.0 \
    mlxtend==0.14.0 \
    networkx==2.2
RUN apt install -y graphviz && \
    pip install pydotplus==2.0.2

ARG MATPLOTLIBRC=$PYTHON_ROOT/lib/python3.6/site-packages/matplotlib/mpl-data/matplotlibrc
RUN pip install matplotlib==3.0.2 && \
    sed -i -r -e 's/#(font.serif *: *)/\1TakaoPMincho, /' $MATPLOTLIBRC && \
    sed -i -r -e 's/#(font.sans-serif *: *)/\1TakaoPGothic, /' $MATPLOTLIBRC
RUN pip install \
    seaborn==0.9.0 \
    bokeh==1.0.4 \
    matplotlib-venn==0.11.5 \
    plotly==3.6.0

RUN pip install notebook==5.7.4 \
    && jupyter notebook --generate-config \
    && sed -i -e "s/#c.NotebookApp.token = '<generated>'/c.NotebookApp.token = 'jupyter'/" /root/.jupyter/jupyter_notebook_config.py
RUN mkdir /root/.jupyter/custom
COPY my-light.css /root/.jupyter/custom/
RUN cd /root/.jupyter/custom \
    && cp my-light.css custom.css
# COPY my-dark.css /root/.jupyter/custom/
# RUN cd /root/.jupyter/custom \
#     && cp my-dark.css custom.css
# RUN pip3 install jupyterthemes==0.19.6 \
#     && jt -t monokai -f source -fs 12 -nf sourcesans -nfs 10 -tf sourcesans -tfs 14 -dfs 12 -ofs 12 -mathfs 100 -m auto -cursw 2 -cellw 80% -lineh 130 -altmd -T \
#     && cd /root/.jupyter/custom \
#     && mv custom.css theme.css \
#     && cat my.css theme.css > custom.css
RUN pip install ipywidgets==7.4.2 && \
    jupyter nbextension enable --py widgetsnbextension && \
    pip install jupyter_contrib_nbextensions==0.5.1 \
    && jupyter contrib nbextension install \
    && jupyter nbextension enable code_prettify/code_prettify \
    && jupyter nbextension enable codefolding/main \
    && jupyter nbextension enable collapsible_headings/main \
    && jupyter nbextension enable exercise2/main \
    && jupyter nbextension enable hide_input/main \
    && jupyter nbextension enable hinterland/hinterland \
    && jupyter nbextension enable livemdpreview/livemdpreview \
    && jupyter nbextension enable ruler/main \
    && jupyter nbextension enable toc2/main \
    && jupyter nbextension enable varInspector/main
RUN jupyter notebook --allow-root --no-browser --ip=0.0.0.0 &
RUN cd /root/.jupyter/nbconfig \
    && sed -i "2i   \"hinterland\": {\n    \"hint_delay\": \"500\"\n  }," ./notebook.json \
    && sed -i "2i   \"toc2\": {\n    \"toc_window_display\": true,\n    \"oc_window_display\": true,\n    \"skip_h1_title\": true\n  }," ./notebook.json
RUN pip install \
    nbdime==1.0.4 \
    yapf==0.25.0

# CLEAN UP
RUN apt clean && \
    rm -rf /var/lib/apt/lists/*

# SET WORKDIR
VOLUME $HOME/workspace
WORKDIR $HOME/workspace
LABEL version=$VERSION maintainer=$MAINTAINER
