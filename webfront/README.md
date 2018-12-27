# webfront

> our-home-refrigerator web front ~ PROGRAPHEED

## Build Setup

``` bash
# install dependencies
npm install

# serve with hot reload at localhost:8080
npm run dev

# build for production with minification
npm run build

# build for production and view the bundle analyzer report
npm run build --report

# run e2e tests
npm run e2e

# run all tests
npm test
```

For a detailed explanation on how things work, check out the [guide](http://vuejs-templates.github.io/webpack/) and [docs for vue-loader](http://vuejs.github.io/vue-loader).


## vue-cli 사용하기

### 폴더구조 살펴보기

* build/ : webpack 빌드 관련 설정이 모여 있는 디렉토리입니다.
* config/ : 프로젝트에서 사용되는 설정이 모여 있는 디렉토리입니다.
    - dev.env.js : npm start 시 적용되는 설정입니다.
    - prod.env.js : npm run build 로 배포 버전에 적용되는 설정입니다.
* dist/ : 배포버전의 Vue 어플리케이션 파일들이 모여 있는 디렉토리입니다. npm run build 명령어 실행시 생성됩니다.
* node_modules/ : npm으로 설치되는 서드파트 라이브러리들이 모여 있는 디렉토리입니다.
* src/ : 실제 대부분의 코딩이 이루어지는 디렉토리입니다.
    - assets/ : 이미지 등.. 어플리케이션에서 사용되는 파일들이 모여 있는 디렉토리입니다.
    - components/ : Vue 컴포넌트들이 모여 있는 디렉토리입니다.
    - router/ : vue-router 설정을 하는 디렉토리입니다.
    - App.vue : 가장 최상위 컴포넌트입니다.
    - main.js : 가장 먼저 실행되는 javascript 파일입니다. Vue 인스턴스를 생성하는 역활을 합니다.
* index.html : 어플리케이션의 뼈대가 되는 html 파일입니다.


### npm run dev

npm run dev를 실행하면 아래 명령어를 실행합니다.    
`webpack-dev-server --inline --progress --config build/webpack.dev.conf.js`

`webpack.dev.conf.js`와 `webpack.base.conf.js`는 webpack의 설정 파일로, 두 설정 파일에 따라 webpack이 프로젝트를 빌드하게 됩니다.

(참고: [[webpack]webpack4 사용하기](http://beomy.tistory.com/42))


### index.html

어플리케이션의 뼈대가 되는 html이다. 

```javascript
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width,initial-scale=1.0">
    <title>my-project</title>
  </head>
  <body>
    <div id="app"></div>
    <!-- built files will be auto injected -->
  </body>
</html>
```

`<div id="app"></div>`에 Vue 컴포넌트들이 마운팅. `<div id="app"></div>`에 마운팅 되는 이유는 main.js를 살펴보면 알 수 있음.


### main.js

```javascript

// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
 
Vue.config.productionTip = false
 
/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
```

`main.js`는 Vue 인스턴스(`new Vue()`)를 생성합니다. `el: '#app'`이 정의 되어 `index.html`의 `<div id="app"></div>`에 Vue 컴포넌트들이 마운팅되게 됩니다.


Vue 인스턴스를 살펴보면,

* el: '#app' : id가 app인 html tag에 Vue 컴포넌트가 마운팅 됩니다.
* router : vue-router를 사용할 수 있게 합니다.
* components: { App } : App 컴포넌트를 사용합니다.
* template: '<App />' : #app에 마운팅 되는 컴포넌트는 <App /> 입니다.



### App.vue



즉, 
1. index.html에 있는 id가 `app`인 div에 Vue 컴포넌트를 마운팅한다.
2. 어디에 마운팅할지는 main.js에서 생성한 Vue 인스턴스에서 설정한다.










