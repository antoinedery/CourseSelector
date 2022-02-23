import { Component, ElementRef, ViewChild } from '@angular/core';

@Component({
  selector: 'app-home-page',
  templateUrl: './home-page.component.html',
  styleUrls: ['./home-page.component.scss']
})
export class HomePageComponent {
  @ViewChild("usernameInput") usernameInput!: ElementRef;
  @ViewChild("passwordInput") passwordInput!: ElementRef;
  @ViewChild("dobInput") dobInput!: ElementRef;
  @ViewChild("emailInput") emailInput!: ElementRef;
  username:string = '';
  password:string = '';
  dob:string = '';
  email:string='';

  submit():void {
    this.username = this.usernameInput.nativeElement.value;
    this.password = this.passwordInput.nativeElement.value;
    this.dob = this.dobInput.nativeElement.value;
    this.email = this.emailInput.nativeElement.value;
  }

}
