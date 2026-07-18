let accessToken:string | null = null;

export const tokenService={

    getToken(){

        return accessToken;

    },

    setToken(token:string){

        accessToken=token;

    },

    clearToken(){

        accessToken=null;

    }

};