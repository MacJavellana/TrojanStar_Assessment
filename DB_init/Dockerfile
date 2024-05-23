FROM mcr.microsoft.com/mssql/server:2019-CU13-ubuntu-20.04

WORKDIR /usr/src/app

# Copy initialization scripts
COPY . /usr/src/app

ENV ACCEPT_EULA Y
ENV MSSQL_SA_PASSWORD YourStrong!Passw0rd



EXPOSE 1433

# Run Microsoft SQL Server and initialization script (at the same time)
CMD /bin/bash ./entrypoint.sh