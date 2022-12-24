FROM nginx:alpine
RUN apk add --no-cache esh openssl
COPY nginx-entrypoint.sh .
COPY default.conf.esh /etc/nginx/
ENV TZ="Europe/Moscow"
RUN chmod +x nginx-entrypoint.sh
ENTRYPOINT ["./nginx-entrypoint.sh"]