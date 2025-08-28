# ====== BUILD STAGE ======
FROM maven:3.9.6-eclipse-temurin-17 AS builder

WORKDIR /app

COPY ayush/pom.xml .
COPY ayush/mvnw .
COPY ayush/mvnw.cmd .
COPY ayush/.mvn .mvn

RUN ./mvnw dependency:go-offline -B

COPY ayush/src ./src

RUN ./mvnw clean package -DskipTests

# ====== RUNTIME STAGE ======
FROM eclipse-temurin:17-jre-alpine

WORKDIR /app

COPY --from=builder /app/target/*.jar app.jar

EXPOSE 8080

ENTRYPOINT ["java", "-jar", "app.jar"]
