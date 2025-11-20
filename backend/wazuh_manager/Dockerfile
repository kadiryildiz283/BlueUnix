FROM wazuh/wazuh-manager:4.7.2

# Konfig dosyasını imajın içine kopyala
COPY filebeat.yml /etc/filebeat/filebeat.yml

# İzinleri "root" ve "sadece okunabilir" yap (Filebeat bunu şart koşar)
USER root
RUN chmod 644 /etc/filebeat/filebeat.yml && \
    chown root:root /etc/filebeat/filebeat.yml
