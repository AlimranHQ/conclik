# Conclik Message Protocol

Version: 1.0
Status: Official

---

## Purpose

Define how every component communicates.

---

## Standard Message

Sender

Receiver

Message Type

Payload

Metadata

Timestamp

Trace ID

---

## Rules

Messages are immutable.

Every message has a unique Trace ID.

Messages never bypass the Event Bus.

Failures must return structured errors.

