# ====== BUILD STAGE ======
FROM maven:3.9.6-eclipse-temurin-17 AS builder

WORKDIR /app

# Copy project files from ayush folder
COPY ayush/pom.xml .
COPY ayush/mvnw .
COPY ayush/mvnw.cmd .
COPY ayush/.mvn .mvn

# Download dependencies
RUN ./mvnw dependency:go-offline -B

# Copy source code
COPY ayush/src ./src

# Build the application (skip tests for faster builds, remove -DskipTests if you want tests)
RUN ./mvnw clean package -DskipTests

# ====== RUNTIME STAGE ======
FROM eclipse-temurin:17-jre-alpine

WORKDIR /app

# Copy built jar from builder stage
COPY --from=builder /app/target/*.jar app.jar

EXPOSE 8080

ENTRYPOINT ["java", "-jar", "app.jar"]
