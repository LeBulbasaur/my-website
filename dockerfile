FROM golang:1.21-bookworm AS builder

WORKDIR /app

COPY go.mod go.sum ./
RUN go mod download

COPY . .

RUN templ generate

RUN CGO_ENABLED=0 GOOS=linux go build -o app .

FROM debian:bookworm

WORKDIR /app
COPY --from=builder /app/app .

EXPOSE 8080

CMD ["./app"]