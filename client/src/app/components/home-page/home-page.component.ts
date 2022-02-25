import { Component, ElementRef, ViewChild } from '@angular/core';
import { User } from '@app/classes/user';
import { ClientSocketService } from '@app/services/client-socket.service';

@Component({
  selector: 'app-home-page',
  templateUrl: './home-page.component.html',
  styleUrls: ['./home-page.component.scss'],
})
export class HomePageComponent {
  @ViewChild('usernameInput') usernameInput!: ElementRef;
  @ViewChild('passwordInput') passwordInput!: ElementRef;
  @ViewChild('dobInput') dobInput!: ElementRef;
  @ViewChild('emailInput') emailInput!: ElementRef;
  @ViewChild('coursesInput') coursesInput!: ElementRef;
  test: string[] = [];

  constructor(private clientSocketService: ClientSocketService) {
    this.getList();
  }

  submit(): void {
    const user: User = {
      username: '',
      password: '',
      dob: '',
      email: '',
      courses: '',
    };
    user.username = this.usernameInput.nativeElement.value;
    user.password = this.passwordInput.nativeElement.value;
    user.dob = this.dobInput.nativeElement.value;
    user.email = this.emailInput.nativeElement.value;
    user.courses = this.coursesInput.nativeElement.value;
    if (
      user.username.length < 0 ||
      user.password.length < 0 ||
      user.dob.length < 0 ||
      user.email.length < 0 ||
      user.dob.length < 0 ||
      user.courses.length < 0
    )
      return;
    this.clientSocketService.sendDataToServer(user);
  }

  getList(): void {
    this.clientSocketService.getList();
  }
}
