FROM wazuh/wazuh-manager:4.7.2

# Filebeat ayarını düzelt: SSL doğrulamasını kapat
RUN echo "output.elasticsearch.ssl.verification_mode: none" >> /etc/filebeat/filebeat.yml

# İzinleri düzelt (Filebeat root yetkisi ister)
USER root
RUN chmod 600 /etc/filebeat/filebeat.yml
RUN chown root:root /etc/filebeat/filebeat.yml
