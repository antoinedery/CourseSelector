import { Injectable } from '@angular/core';
import { User } from '@app/classes/user';
import { io, Socket } from 'socket.io-client';
import { environment } from 'src/environments/environment';
@Injectable({
  providedIn: 'root'
})
export class ClientSocketService {
  socket: Socket;
  id: string = '';
  constructor() { 
    this.socket = io(environment.serverUrl, { transports: ['websocket'], upgrade: false });
  }

  sendDataToServer(user:User):void{
    this.socket.emit("launchProcess", user);
  }
}
