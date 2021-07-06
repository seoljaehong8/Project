FROM node:10.19.0

# 이미지 내에서 명령어를 실행할(현 위치로 잡음) 디렉토리 설정
WORKDIR /home/node/app

# 파일복사
COPY package*.json ./
COPY . .

RUN npm install
RUN npm install -g @vue/cli
RUN npm install vuex

# 컨테이너 실행시 실행할 명령어
CMD ["npm", "run", "serve"]
